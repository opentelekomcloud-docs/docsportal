import "@/styles/global.css";
import "@telekom-ods/react-ui-kit/style.css";
import Header from '@/components/Header';
import SideNavigation from '@/components/SideNavigation';
import Footer from '@/components/Footer';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" sizes="any" />
      </head>
      <body>
        <Header></Header>
        <main>
          <SideNavigation></SideNavigation>
          {children}
        </main>
        <Footer></Footer>
      </body>
    </html>
  )
}
