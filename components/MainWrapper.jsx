'use client';

import React from "react";
import styles from '@/styles/MainWrapper.module.css';


export default function MainWrapper({ children }) {
  return (
    <main className={styles.wrapper}>
      {children}
    </main>
  );
}
