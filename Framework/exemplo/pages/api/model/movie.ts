import { prisma } from "@/db";

export async function createmoviemodel( _name:string , _releasedate:string , _imageURL:string , _description:string ) {
    const movie = await prisma.movie.create({ 
        data:{
            name: _name,
            releasedate: _releasedate,
            imageURL: _imageURL,
            description: _description


        }
    })
    return movie;
}


export async function findmoviemodelbyname (_name:string ){

    const movie = await prisma.movie.findUnique({
        where: {
            name : _name
        }
    
    });
    return movie;
    
}
