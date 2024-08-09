import Head from "next/head"
import style from '@/styles/Createmovie.module.css'

export default function createMovie(){

    return(
        <main  className='flex min-h-screen flex-col'>
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <div>
                <form className={style.formcontainer} >
                    <input className={style.Nome} type="text" placeholder="Nome"/>
                    <p className={style.date}>Data de lançamento<input type="date"/></p>
                     <p className={style.image}>imagem: <input type="file"/></p>
                     <input className= {style.input} type="text" placeholder="Descrição do filme" />
                     <br /><br />
                     <input className={style.button} type="button" value="enviar" />
                </form>
            </div>
        </main>
    )
}