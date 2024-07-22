import style from '@/styles/login.module.css'
import Head from 'next/head';

export default function loginPage(){
    return(

        <main className='flex min-h-screen flex-col'>
            <Head>
                <title>login</title>

            </Head>

            <form className={style.container}>
                <input className={style.Nome} type="text" placeholder='Nome de usuario'/>
                <br /><br />
                <input className={style.password} type="password" placeholder='senha'/>
                <br /><br />
                <input className={style.button} type="submit" value="login"/>
            </form>
        </main>
    );
}