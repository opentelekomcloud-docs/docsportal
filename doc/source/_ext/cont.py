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

import otc_metadata.services

LOG = logging.getLogger(__name__)


class navigator(nodes.General, nodes.Element):
    pass


class service_group(nodes.General, nodes.Element):
    pass


class container_item(nodes.General, nodes.Element):
    pass


METADATA = otc_metadata.services.Services()


class ServiceGroup(Directive):
    node_class = service_group
    option_spec = {
        'class': directives.unchanged,
        'service_category': directives.unchanged_required,
        'environment': directives.unchanged_required
    }

    has_content = False

    def run(self):
        node = self.node_class()
        node['service_category'] = self.options.get('service_category')
        node['environment'] = self.options.get('environment', 'public')
        node['class'] = self.options.get('class', 'navigator-container')
        return [node]


class Navigator(Directive):
    node_class = navigator
    option_spec = {
        'class': directives.unchanged,
        'document_type': directives.unchanged,
        'environment': directives.unchanged_required
    }

    has_content = False

    def run(self):
        node = self.node_class()
        node['document_type'] = self.options['document_type']
        node['environment'] = self.options.get('environment', 'public')
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
    data = f'<div class="{node["class"]} container-docsportal">'

    for cat in METADATA.service_categories:
        category = cat["name"]
        category_title = cat["title"]
        data += (
            f'<div class="card item-docsportal">'
            f'<div class="card-body">'
            f'<h5 class="card-title">{category_title}</h5></div>'
            f'<ul class="list-group list-group-flush">'
        )
        for k, v in METADATA.services_with_docs_by_category(
                category=category, environment=node['environment']).items():
            title = v["service_title"]
            for doc in v.get("docs", []):
                if "link" not in doc:
                    continue
                if "type" not in doc or doc["type"] != node["document_type"]:
                    continue
                title = doc["service_title"]
                link = doc.get("link")
                img = v["service_type"]
                data += (
                    f'<li class="list-group-item"><a href="{link}">'
                    f'<div class="row">'
                    f'<div class="col-2">'
                    f'<img src="_static/images/services/{img}.svg">'
                    f'</div>'
                    f'<div class="col-10">{title}</div>'
                    f'</div></a></li>'
                )

        data += '</ul></div>'

    data += '</div>'

    self.body.append(data)
    raise nodes.SkipNode


def service_group_html(self, node):
    # This method renders containers per each service of the category with all
    # links as individual list items
    data = '<div class="container-docsportal">'
    for k, v in METADATA.services_with_docs_by_category(
            node['service_category'], environment=node['environment']).items():
        if not v.get("docs"):
            continue
        title = v["service_title"]
        data += (
            f'<div class="card item-docsportal">'
            f'<div class="card-body"><h5 class="card-title">'
            f'{title}</h5></div>'
            f'<ul class="list-group list-group-flush">'
        )
        for doc in v.get("docs", []):
            if not "link" in doc:
                continue
            title = doc["title"]
            link = doc.get("link")
            data += (
                f'<li class="list-group-item"><a href="{link}">'
                f'<div class="row">'
                f'<div class="col-md-10 col-sm-10 col-xs-10">{title}</div>'
                f'</div></a></li>'
            )
        # Row end
        data += '</ul></div>'
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
