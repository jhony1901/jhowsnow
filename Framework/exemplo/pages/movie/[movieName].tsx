import { checktoken } from '@/services/tokenConfig';
import styles from '@/styles/movie.module.css'
import { getCookie } from 'cookies-next';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';



export default function movie({ movieName }: any) {

    const router = useRouter();
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

    async function formSubmit(event: any) {
        event.preventDefault()
        try {

            const cookieAuth = getCookie('authorization')
            const tokenInfos = checktoken(cookieAuth);

            const response = await fetch(`/api/action/rating/create`, {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(
                    {
                        value: Number(formRating.value),
                        comment: formRating.comment,
                        username: tokenInfos.username,
                        moviename: movieName

                    }
                )
            });


            const responseJson = await response.json();

            alert(responseJson.message)
            router.reload();

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
                            <h1 className={styles.commentTitle}>Comentários</h1>
                            {
                                data.ratings.map((rating: any) => (
                                    <div className={styles.commentCard}>
                                        <div className={styles.commentInfos}>
                                            <label>{rating.user.username}</label>
                                            <label className={styles.valueR}>({rating.value}) / 5 Recomendação</label>
                                        </div>
                                        <br />
                                        <div className={styles.commentBox}>
                                            <label>{rating.coment}</label>
                                        </div>
                                    </div>


                                ))
                            }
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