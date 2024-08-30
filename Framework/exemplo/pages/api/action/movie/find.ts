import { NextApiRequest , NextApiResponse } from "next";
import { findmoviebyname, selectMovies } from "../../controller/moviecontroler";

export default async ( req: NextApiRequest , res: NextApiResponse) =>{
    if (req.method != 'GET') {
        return res.status(403).json ( {message: 'method not allowed' });
        
    }
    const { name }:any = req.query;

    const response = await findmoviebyname(name);

    if ( response.status == 200){
        return res.status ( response.status).json( { message: response.message ,  data: response.data});
    }
    else{
        return res.status(  response.status ).json( { message: response.message});
    }
}