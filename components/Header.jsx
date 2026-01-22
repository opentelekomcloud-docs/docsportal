'use client';

import React, { useLayoutEffect, useRef } from "react";
import Link from "next/link";
import { usePathname } from 'next/navigation'
import { useRouter } from 'next/navigation'
import styles from '@/styles/Header.module.css';
import { ODSStandardGlobalHeader, ODSBadgeIcon, ODSGlobalHeaderTabletMobileMenu, ODSGlobalHeaderMenu, ODSGlobalHeaderMenuLabel, ODSGlobalHeaderSecondaryMenu, ODSGlobalHeaderMenuButton } from "@telekom-ods/react-ui-kit";

export default function Header() {
  // we use the inital layouteffect to get the size of the header
  // this is then used to calculate the header hide and
  // configure the padding-top of the main component
  // to move the main part down. Otherwise the header
  // would overlap the content.
  useLayoutEffect(() => {
    const headerEl = document.querySelector(".ODSStandardGlobalHeader");

    const update = () => {
      const h = headerEl.getBoundingClientRect().height;
      document.documentElement.style.setProperty("--app-header-h", `${h}px`);
    };

    update();

    const ro = new ResizeObserver(update);
    ro.observe(headerEl);

    return () => ro.disconnect();
  }, []);

  return (
    <ODSStandardGlobalHeader
      applicationName="T Cloud Public"
      logoProps={{
        "aria-label": "T Cloud Public",
        href: "https://www.telekom.com/",
        target: "_blank",
        title: "T Cloud Public",
        type: "primary",
      }}
      menuItems={[
        {
          href: "#1",
          label: "Services",
          selected: true,
        },
        {
          href: "#2",
          label: "Developers",
        }
      ]}
      primaryLinkItems={[
        {
          external: true,
          icon: "navigation-external-link-type-standard",
          linkText: "Console",
        },
        {
          external: true,
          icon: "navigation-external-link-type-standard",
          linkText: "Community Portal",
        },
        {
          external: true,
          icon: "navigation-external-link-type-standard",
          linkText: "Architecture Center",
        },
      ]}
  // menuSlot={
  //   <ODSGlobalHeaderMenu>
  //     <ODSGlobalHeaderMenuLabel href="#2" label="Topic" />
  //     <ODSGlobalHeaderMenuLabel href="#3" label="Topic" />
  //   </ODSGlobalHeaderMenu>
  // }
      secondaryMenuItems={[
        {
          icon: "search-type-standard",
          label: "Search",
          selected: true,
        }
      ]}
  secondaryMenuSlot={
    <ODSGlobalHeaderSecondaryMenu aria-label="Secondary">
      <ODSGlobalHeaderTabletMobileMenu
        applicationName="T Cloud Public"
        trigger={
          <ODSGlobalHeaderMenuButton icon="menu-type-standard" label="Menu" />
        }
        menuItems={[
          {
            label: "Level 1 Expandable",
            variant: "cascade",
            cascadeMenuProps: {
              items: [
                { label: "Level 2" },
                { label: "Level 2" },
                {
                  label: "Level 2 Expandable",
                  cascadeMenuProps: {
                    items: [{ label: "Level 3" }, { label: "Level 3" }],
                  },
                  iconAfter: "navigation-right-type-standard",
                },
              ],
            },
            iconAfter: "navigation-right-type-standard",
          },
          { label: "Level 1" },
        ]}
        linkItems={[
          {
            linkText: "Link 1",
            icon: "navigation-external-link-type-standard-size-small",
            external: true,
          },
          {
            linkText: "Link 2",
            icon: "navigation-external-link-type-standard-size-small",
            external: true,
          },
          {
            linkText: "Link 3",
          },
        ]}
      />
    </ODSGlobalHeaderSecondaryMenu>
  }
/>
  );
}