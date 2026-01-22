'use client';

import React from "react";
import Link from "next/link";
import { usePathname } from 'next/navigation'
import { useRouter } from 'next/navigation'
import styles from '@/styles/Footer.module.css';
import { ODSFooter, ODSFooterMenuItem } from "@telekom-ods/react-ui-kit";

function Footer({}) {
  return (
    <ODSFooter
        copyrightText="© Deutsche Telekom AG"
        logoProps={{
            'aria-label': 'Telekom Home',
            href: 'https://www.telekom.com/',
            target: '_blank',
            title: 'Telekom Home',
            type: 'secondary'
        }}
        variant="standard"
        >
        <ODSFooterMenuItem
            href="/menu-item-text-1"
            text="Menu Item Text"
        />
        <ODSFooterMenuItem
            href="/menu-item-text-2"
            text="Menu Item Text"
        />
        <ODSFooterMenuItem
            href="/menu-item-text-3"
            text="Menu Item Text"
        />
    </ODSFooter>
  );
}

export default Footer;