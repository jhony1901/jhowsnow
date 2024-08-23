
import { createmoviemodel , findmoviemodelbyname } from "../model/movie";

export async function createmovie( _name: string , _releasedate: string , _imageURL: "" , _videoURL:"" , _description :"") {
    try{
        const moviebyname = await findmoviemodelbyname(_name);

        if (moviebyname != undefined) {
            return{ status:403, message : "name already registered"};
        }
        const response = await createmoviemodel( _name , _releasedate  , _imageURL , _description, _videoURL );

        return {status:201, message:'movie registered', data:response };

    }
    catch (err){
        return { status:500, message: 'Something went wrong' };

    }
    
}