import { createRatingModel , findRatingUser, updateRating } from "../model/rating";
import { findusermodelbyusername } from "../model/user";
import { findmoviemodelbyname } from "../model/movie";

export async function createRating(_value: number, _username: string, _moviename: string, _coment = "") {
    try {
        const userByUsername = await findusermodelbyusername(_username);

        if (userByUsername == undefined) {
            return { status: 404, message: 'User not found ' }
        }
        const movieByname = await findmoviemodelbyname(_moviename)

        if (movieByname == undefined) {
            return { status: 404, message: 'Movie not found ' };
        }
        const ratingByUser = await findRatingUser(userByUsername.id, movieByname.id);

        if (ratingByUser != undefined) {
            const updating = await updateRating(ratingByUser.id , _value, _coment);


            return { status:200, message: 'Rating update' , data:updating};
        }


        const response = await createRatingModel(_value, _coment, userByUsername.id, movieByname.id);

        return { status: 200, message: 'Rating created', data: response };

    }
    catch (err) {
        return { status: 500, message: 'something went wronk' };
    }
}