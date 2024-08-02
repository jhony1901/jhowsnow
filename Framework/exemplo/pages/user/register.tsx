import Style from '@/styles/register.module.css';
import Head from 'next/head';
import { useState } from 'react';
import Link from 'next/link';

export default function registerpage() {
    const [formData, setFormData] = useState(
        {

            name: "",
            username: "",
            password: "",
            confirmpassword: "",
            cpf: ""

        }
    );
    function handleFormEdit(event: any, field: string) {
        setFormData({
            ...formData,
            [field]: event.target.value
        })

    }
    async function formSubmit(event: any) {
        event.preventDefault()
        console.log(formData);

        try {
            const response = await fetch(`/api/action/user/create`, {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(formData)
            });
            const responseJson = await response.json();

            alert(`${response.status} \n${responseJson}`);
        }
        catch (err) {
            console.log(err);
        }
    }
    return (
        <main id={Style.main} className='flex min-h-screen flex-col'>
            <Head>
                <title>cadastro</title>
            </Head>

            <form className={Style.container} onSubmit={formSubmit}>
                <div>
                    <h2>Criar conta</h2>
                    <input type="text" placeholder=' name' onChange={(event) => { handleFormEdit(event, 'name') }} />
                    <br /><br />
                    <input type="text" placeholder='username' onChange={(event) => { handleFormEdit(event, 'ussername') }} />
                    <br /><br />
                    <input type="password" placeholder='senha' onChange={(event) => { handleFormEdit(event, 'password') }} />
                    <br /><br />
                    <input type="password" placeholder='confirmar senha' onChange={(event) => { handleFormEdit(event, 'confirmpasswod') }} />
                    <br /><br />
                    <input type="text" placeholder='cpf' onChange={(event) => { handleFormEdit(event, 'cpf') }} />
                    <br /> <br />

                    <Link href={`/user/login`} >ja tenho uma conta </Link>
                    <input className={Style.button} type="submit" value='enviar' />

                </div>
            </form>
        </main>
    );
}