import  Style  from '@/styles/register.module.css';
import Head from 'next/head';

export default function registerpage() {
        return(
            <main className='flex min-h-screen flex-col'>
                <Head>
                    <title>cadastro</title>
                </Head>

                <div className={Style.container}>
                    <input type="text" />
                    <input type="email" name="" id="" />
                    
                </div>
            </main>
        );
}