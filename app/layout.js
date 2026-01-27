import "@/styles/global.css";
import "@telekom-ods/react-ui-kit/style.css";
import Header from '@/components/Header';
import MainWrapper from '@/components/MainWrapper';
import Footer from '@/components/Footer';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" sizes="any" />
      </head>
      <body>
        <Header></Header>
        <MainWrapper>{children}</MainWrapper>
        <Footer></Footer>
      </body>
    </html>
  )
}
