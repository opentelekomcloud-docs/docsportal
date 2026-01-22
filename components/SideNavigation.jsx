'use client';

import React from "react";
import Link from "next/link";
import { usePathname } from 'next/navigation'
import { useRouter } from 'next/navigation'
// import styles from '@/styles/SideNavigation.module.css';
import { ODSSideNavigation, ODSAvatar } from "@telekom-ods/react-ui-kit";

function SideNavigation({}) {
    return (
        <div
        style={{
            height: '650px'
        }}
        >
        <ODSSideNavigation
            bottomBarCollapsedSlot={<ODSAvatar icon="light-dark-mode-type-bold" name="Erika Mustermann" showBackground size="large" variant="icon"/>}
            bottomBarExpandedSlot={<div style={{display: 'flex', justifyContent: 'space-between', width: '100%'}}><ODSAvatar icon="light-dark-mode-type-bold" name="Erika Mustermann" showBackground size="large" variant="icon"/><React.Memo label="Log Out" size="small" variant="outline"/></div>}
            items={[
            {
                icon: 'search-type-bold',
                label: 'Label 1',
                lockIcon: true,
                showBadge: true
            },
            {
                icon: 'search-type-bold',
                label: 'Label 2',
                showBadge: false
            },
            {
                icon: 'search-type-bold',
                label: 'Label 3',
                subItems: [
                {
                    label: 'Label 3.1',
                    showBadge: true
                },
                {
                    label: 'Label 3.2',
                    showBadge: true
                },
                {
                    label: 'Label 3.3',
                    showBadge: false
                }
                ]
            },
            {
                icon: 'loop-type-bold',
                label: 'Label 4',
                showBadge: false
            },
            {
                icon: 'search-type-bold',
                label: 'Label 5',
                showBadge: false
            },
            {
                icon: 'search-type-bold',
                label: 'Label 6',
                subItems: [
                {
                    label: 'Label 6.1',
                    lockIcon: true,
                    showBadge: false
                }
                ]
            },
            {
                icon: 'print-type-bold',
                label: 'Label 7',
                showBadge: false
            }
            ]}
            onExpandedChanged={function S6(){}}
            onItemClicked={function S6(){}}
        />
        </div>

    );
}

export default SideNavigation;