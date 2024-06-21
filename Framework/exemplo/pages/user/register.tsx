import  Style  from '@/styles/register.module.css';
import Head from 'next/head';

export default function registerpage() {
        return(
            <main id={Style.main} className='flex min-h-screen flex-col'>
                <Head>
                    <title>cadastro</title>
                </Head>

                <form className={Style.container}>
                    <div>  
                    <h2>Criar conta</h2>
                     
                    <input type="text" placeholder='user name'/>
                    <br /><br />
                    <input type="password" placeholder='senha'/>
                    <br /> <br />
                    <input type="password" placeholder='confirmar senha'/>
                    <br /><br />
                    <input type="email"placeholder='email'/>

                    <br /><br />
                    <input className={Style.button} type="submit" value='enviar' />
                    
                    </div>
                </form>
            </main>
        );
}