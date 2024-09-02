import styles from '@/styles/movie.module.css'
import { useState, useEffect } from 'react';

export default function movie({ movieName }: any) {
    const [ data, setData ]: any = useState();

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