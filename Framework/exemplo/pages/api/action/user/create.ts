import {NextApiRequest , NextApiResponse} from "next";
import {createUser} from "../../controller/Usercontroller";

export default async ( req : NextApiRequest, res : NextApiResponse) =>{

    if (req.method != 'Post'){
        return res.status(403).json({message : 'method not allowed'});
    }
    
    const { name , username, password ,confirmpassword ,cpf} = req.body;

    const response : any = await createUser(username , password ,confirmpassword ,cpf ,name );

    if ( response.message != undefined){
        return res.status(403).json(response);
    }
    else
       return res.status(201).json(response);
}