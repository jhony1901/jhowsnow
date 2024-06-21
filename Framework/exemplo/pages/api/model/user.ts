import { prisma } from "@/db";

export async function createrusermodel( _name:string , _username:string , _password:string , _cpf:string) {
    const user= await prisma.user.create({ 
        data:{
            name: _name,
            username: _username,
            password: _password,
            cpf: _cpf
        }
    })
    return user;
}