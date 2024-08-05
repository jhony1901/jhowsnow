
import { getCookie } from "cookies-next";
import { checktoken } from "@/services/tokenConfig";
import  styles from '@/styles/home.module.css';

export default function Home() {
  return (
    <main  className='flex min-h-screen flex-col'>
        <nav className={styles.navbar}>
            <input className = {styles.text}type="text" />
            <button className={styles.button}></button>
        </nav>

        <div className={styles.maincontainer}>
          <div className={styles.leftcontainer}>

          </div>

        </div>
        <div className={styles.rightcontainer}>


        </div>
    </main>

  )
}


export function getServerSideProps( {req , res }:any){
  try{
      const token = getCookie('authorization' , {req , res} );
      if ( !token) {
          throw new Error ('invaled token');
      }

      checktoken(token);

      return {
          props: {}
      }
  }

  catch (err) {
      return{
        redirect: {
          permanent: false,
          destination: '/',
      },
          props: {}
          
      }
  }
}