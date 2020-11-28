import Head from 'next/head'
import Design from '../Components'
export default function Home({ baseURL }) {
  return (
    <div>
      <Head>
        <title>WiFi App</title>
      
      </Head>
      <Design baseURL={baseURL} />
    </div>
  )
}
