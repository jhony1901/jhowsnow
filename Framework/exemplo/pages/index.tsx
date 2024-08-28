
import { getCookie } from "cookies-next";
import { checktoken } from "@/services/tokenConfig";
import styles from '@/styles/home.module.css';
import { useState, useEffect } from 'react';

export default function Home() {
  //constante para armazenar filme
  const [data, setData]: any = useState(undefined);

  // funcao para receber os dados dos filmes
  async function fetchData() {
    try {
      const response = await fetch(`/api/action/movie/select`, {
        method: 'GET',
      })

      const responseJson = await response.json();

      console.log(responseJson.data);
      setData(responseJson.data);

    }
    catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchData();

  }, [])

  return (

    <main className='flex min-h-screen flex-col'>
      <nav className={styles.navbar}>
        <img className={styles.icon} src="/cinemaicon.jfif" alt="" />
        <input className={styles.searchBar} type="text" />
        <button className={styles.button}>logout</button>
      </nav>

      <div className={styles.maincontainer}>


        <div className={styles.leftcontainer}>
        </div>



        <div className={styles.rightcontainer}>

          {data != undefined && data instanceof Array ?

            data.map(movie => (
              <div className={styles.Card}>
                <img src="/baudamorte.jpg " alt="" className={styles.cardImg} />
                <div className={styles.Cardinfos}>
                  <h2>{movie.name}</h2>
                  <p> {movie.releasedate}</p>
                  <p>Generos</p>
                </div>
              </div>
            ))


            :

            <p>No movies found</p>

          }

        </div>

      </div>


    </main>

  )
}


export function getServerSideProps({ req, res }: any) {
  try {
    const token = getCookie('authorization', { req, res });
    if (!token) {
      throw new Error('invaled token');
    }

    checktoken(token);

    return {
      props: {}
    }
  }

  catch (err) {
    return {
      redirect: {
        permanent: false,
        destination: '/user/login',
      },
      props: {}

    }
  }
}