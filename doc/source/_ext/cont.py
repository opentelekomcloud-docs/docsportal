# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import yaml

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.util import logging

LOG = logging.getLogger(__name__)


class navigator(nodes.General, nodes.Element):
    pass


class service_group(nodes.General, nodes.Element):
    pass


class container_item(nodes.General, nodes.Element):
    pass


YAML_CACHE = {}


class ServiceGroup(Directive):
    node_class = service_group
    option_spec = {
        'class': directives.unchanged,
        'data': directives.unchanged_required,
        'category': directives.unchanged_required
    }

    has_content = False

    def _load_data(self, fpath):
        global YAML_CACHE
        if fpath in YAML_CACHE:
            return YAML_CACHE[fpath]
        data = {}
        try:
            with open(fpath, 'r') as stream:
                data = yaml.safe_load(stream)
        except IOError:
            LOG.warning(
                "Parameters file not found, %s", fpath,
                location=(self.state.document.settings.env.docname, None))
            return
        except yaml.YAMLError as exc:
            LOG.exception(
                exc_info=exc,
                msg="Error while parsing file [%s]." % fpath)
            raise

        YAML_CACHE[fpath] = data
        return data

    def run(self):
        node = self.node_class()
        _, fpath = self.state.document.settings.env.relfn2path(
            self.options['data'])
        data = self._load_data(fpath)
        node['data'] = data['service_categories'][self.options['category']]
        node['class'] = self.options.get('class', 'navigator-container')
        return [node]


class Navigator(Directive):
    node_class = navigator
    option_spec = {
        'class': directives.unchanged,
        'data': directives.unchanged_required,
        'link_type': directives.unchanged
    }

    has_content = False

    def _load_data(self, fpath):
        global YAML_CACHE
        if fpath in YAML_CACHE:
            return YAML_CACHE[fpath]
        data = {}
        try:
            with open(fpath, 'r') as stream:
                data = yaml.safe_load(stream)
        except IOError:
            LOG.warning(
                "Parameters file not found, %s", fpath,
                location=(self.state.document.settings.env.docname, None))
            return
        except yaml.YAMLError as exc:
            LOG.exception(
                exc_info=exc,
                msg="Error while parsing file [%s]." % fpath)
            raise

        YAML_CACHE[fpath] = data
        return data

    def run(self):
        node = self.node_class()
        _, fpath = self.state.document.settings.env.relfn2path(
            self.options['data'])
        self.data = self._load_data(fpath)
        node['data'] = self.data
        node['link_type'] = self.options['link_type']
        node['class'] = self.options.get('class', 'navigator-container')
        return [node]


class ContainerItem(Directive):
    node_class = container_item
    option_spec = {
        'title': directives.unchanged,
        'image': directives.unchanged,
    }

    has_content = True

    def run(self):
        doctree_node = container_item()
        doctree_node['title'] = self.options['title']
        if 'image' in self.options:
            doctree_node['image'] = self.options['image']
        services = []
        for ent in self.content:
            _srv = ent.strip('- ')
            data_parts = _srv.split("|")
            title = data_parts[0]
            href = data_parts[1] if len(data_parts) > 1 else '#'
            services.append(
                dict(
                    title=title,
                    href=href
                )
            )
        doctree_node['services'] = services
        return [doctree_node]


def container_item_html(self, node):
    tmpl = f"""
        <div class="col">
          <div class="card">
            %(img)s
            <div class="card-body">
              <h5 class="card-title">%(title)s</h5>
            </div>
            %(data)s
          </div>
        </div>
        """

    node['data'] = (
        "<ul class='list-group list-group-flush'>" +
        "".join([('<li class="list-group-item"><a href="%(href)s">'
                  '<div class="col-md-10">%(title)s</div>'
                  '</a></li>'
                  % x)
                 for x in node['services']]) +
        "</ul>")
    node['img'] = ''
    if 'image' in node and node['image']:
        node['img'] = (
            f'<img src="{node["image"]}" '
            'class="card-img-top mx-auto">'
        )
    self.body.append(tmpl % node)
    raise nodes.SkipNode


def navigator_html(self, node):
    # This method renders containers of service groups with links to the
    # document of the specified type
    data = f'<div class="{node["class"]} row row-cols-1 row-cols-md-3 g-4">'
    for k, v in node['data']['service_categories'].items():
        data += (
            f'<div class="col"><div class="card">'
            f'<div class="card-body">'
            f'<h5 class="card-title">{v["title"]}</h5></div>'
            f'<ul class="list-group list-group-flush">'
        )
        for srv_k, srv_v in v['services'].items():
            # if service has no proper link for the type - skip it
            link = srv_v.get(node["link_type"], None)
            if not link:
                continue
            img = srv_k
            title = srv_v["title"]
            data += (
                f'<li class="list-group-item"><a href="{link}">'
                f'<div class="row">'
                f'<div class="col-2">'
                f'<img src="_static/images/services/{img}.svg">'
                f'</div>'
                f'<div class="col-10">{title}</div>'
                f'</div></a></li>'
            )
        data += '</ul></div></div>'

    data += '</div>'

    self.body.append(data)
    raise nodes.SkipNode


def service_group_html(self, node):
    # This method renders containers per each service of the category with all
    # links as individual list items
    data = '<div class="row row-cols-1 row-cols-md-3 g-4">'
    for k, v in node['data']['services'].items():
        title = v["title"]
        data += (
            f'<div class="col"><div class="card">'
            f'<div class="card-body"><h5 class="card-title">'
            f'{v["title"]}</h5></div>'
            f'<ul class="list-group list-group-flush">'
        )
        # API-Ref and UMN
        # NOTE(gtema): maybe we want some special icons
        for doc_type in [
            ('api', 'API Reference'),
            ('umn', 'User Manual')
        ]:
            link = v.get(doc_type[0])
            if link:
                title = doc_type[1]
                data += (
                    f'<li class="list-group-item"><a href="{link}">'
                    f'<div class="row">'
                    f'<div class="col-md-10 col-sm-10 col-xs-10">{title}</div>'
                    f'</div></a></li>'
                )

        # all other links
        for link in v.get("links", []):
            data += (
                f'<li class="list-group-item"><a href="{link["url"]}">'
                f'<div class="row">'
                f'<div class="col-md-10 col-sm-10 col-xs-10">{link["title"]}</div>'
                f'</div></a></li>'
            )
        # Row end
        data += '</ul></div></div>'
    data += '</div>'

    self.body.append(data)
    raise nodes.SkipNode


def setup(app):
    app.add_node(container_item,
                 html=(container_item_html, None))
    app.add_node(navigator,
                 html=(navigator_html, None))
    app.add_node(service_group,
                 html=(service_group_html, None))
    app.add_directive("container_item", ContainerItem)
    app.add_directive("navigator", Navigator)
    app.add_directive("service_group", ServiceGroup)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
