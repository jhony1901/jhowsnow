import style from '@/styles/login.module.css'
import { UNSTABLE_REVALIDATE_RENAME_ERROR } from 'next/dist/lib/constants';
import Head from 'next/head';
import Link from 'next/link';
import { useState } from 'react';


export default function loginPage(){

    const [ formData , setFormData ] = useState(
        {
            username: '',
            password: ''
        }
    );

    function handlerformEdit(event:any , field:string){
        setFormData({
            ...formData,
            [field] : event.target.value
        });
    }


    async function formSubmit (event:any) {
        event.preventDefault();
        console.log(formData);

        try{
            const response = await fetch(`/api/action/user/login` ,{
                method:'POST',
                headers:{'Content-type': 'application/json'},
                body: JSON.stringify(formData)
            });


            const responsejson = await response.json();

            alert(`${response.status}\n${responsejson.message}\n${responsejson.token}`);
        }



        catch(err){
            console.log(err)
        }
    }   
     
    

    return(
    

        <main className='flex min-h-screen flex-col'>
            <Head>
                <title>login</title>

            </Head>

            <form className={style.container} onSubmit={formSubmit}>
            
                <input className={style.Nome} type="text" placeholder='Nome de usuario' onChange={(event) => {handlerformEdit(event , 'username')}}/>
                <br /><br />
                <input className={style.password} type="password" placeholder='senha'onChange={(event) => {handlerformEdit(event , 'password')}}/>
                <br /><br />
                <input className={style.button} type="submit" value="login"/>

                <Link className={style.criarconta} href={`/user/register`}>Criar uma conta</Link>
            </form>
        </main>
    );
}