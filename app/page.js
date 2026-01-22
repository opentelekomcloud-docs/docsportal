'use client';

import Image from "next/image";
import { ODSButton } from "@telekom-ods/react-ui-kit";

export default function Home() {
  return (
    <div>
      <ODSButton
        buttonIcon="happy-person-type-standard"
        buttonType="standard"
        label="Button Label"
        size="large"
        variant="primary"
      />
  </div>
  );
}
