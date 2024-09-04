
import {prisma } from '@/db'


export async function createRatingModel(_value:number , _coment:string , _userId:number , _movieId:number ) {
    const rating = await prisma.rating.create({
        data: {
            value: _value,
            coment: _coment,
            user: {
                connect: {
                    id: _userId
                }
            },
            movie:{
                connect:{
                    id: _movieId
                }
            }
        }
    })
    return rating;
}