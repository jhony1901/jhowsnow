import { checktoken } from '@/services/tokenConfig';
import styles from '@/styles/movie.module.css'
import { getCookie } from 'cookies-next';
import { useState, useEffect } from 'react';



export default function movie({ movieName }: any) {
    const [data, setData]: any = useState();
    const [formRating, setformRating] = useState(
        {
            value: 0,
            comment: ''
        }

    );

    function handleformEdit(event: any, field: string) {
        setformRating({
            ...formRating,
            [field]: event.target.value
        });
    }

    async function formSubmit(event:any) {
        event.preventfefault()
        try {

            const cookieAuth = getCookie('authorization')
            const tokenInfos = checktoken(cookieAuth);

            const response = await fetch(`/api/action/rating/create`, {
                method: 'POST',
                headers: { 'content-type': 'applicatio/json' },
                body: JSON.stringify(
                    {
                        value: Number(formRating.value),
                        comment: formRating.comment,
                        username: tokenInfos.username

                    }
                )
            });


            const responseJson = await response.json();
            alert(responseJson.message)

        } catch (err) {
            console.log(err)
        }
    }


    async function fetchData() {
        try {
            const response = await fetch(`/api/action/movie/find?name=` + movieName, {
                method: 'GET'
            })

            const responsejson = await response.json();
            console.log(responsejson.data);
            setData(responsejson.data)



        }

        catch (err) {
            console.log(err);
        }
    }

    useEffect(() => {
        fetchData();

    }, [])


    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>

            {
                data != undefined ?

                    <div className={styles.page}>
                        <div className={styles.movie}>
                            <img src={data.imageURL} className={styles.Img} />

                            <div className={styles.movieInfos}>
                                <h2>{data.name}</h2>
                                <p>{data.releaseDate} </p>
                                <p>{data.description}</p>
                                <p>Generos</p>

                            </div>

                        </div>

                        <iframe className={styles.video} height="350" src={'https://www.youtube.com/embed/' + data.videoURL}>
                        </iframe>


                        <form className={styles.formRating} onSubmit={formSubmit}>
                            <h2 className={styles.nota}>Digte uma Nota (0 a 5)</h2>
                            <input className={styles.value} type="number" onChange={(e) => { handleformEdit(e, 'value') }} /><br />
                            <textarea className={styles.comment} placeholder="Digite seu comentario" onChange={(e) => { handleformEdit(e, 'comment') }}></textarea>
                            <input className={styles.btnsubmit} type="submit" />
                        </form>

                        <div className={styles.comments}>
                            <div className={styles.commentCard}></div>
                            <div className={ styles.commentInfos}>
                                <p>nome do usuario       (5)  / 5 recomendaçao</p>
                                <label className={styles.commentsbox}>É elogiado por seu desempenho, ergonomia e estilo, sendo considerado um computador gamer portátil de alta qualidade. Ainda assim, é uma ótima solução para quem viaja muito e busca um dispositivo potente.</label>
                                </div>
                        </div>

                    </div>
                    :

                    <p> Erro 404. Não encontrado</p>
            }


        </main>

    );
}

export function getServerSideProps(context: any) {
    const { movieName } = context.query;

    return {
        props: { movieName }
    }
}