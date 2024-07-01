import {createrusermodel , findusermodelbycpf, findusermodelbyusername}  from "../model/user";

export async function createUser(_username:string , _password:string , _confirmPassword:string , _cpf:string , _name = "") {
    // Realizar verificações em atributos Únicos das tabelas.
    // Verificar se os valores já estão cadastrados no banco de dados
    try {
        if( _password != _confirmPassword ) {
            return { message: 'Passwords dont match' };
        }

        //Verificar username e cpf
        const userbycpf = await findusermodelbycpf(_cpf);

        if (userbycpf != undefined ) {
            return{ message : "cpf already registered"};
        }
        const userbyname = await findusermodelbyusername(_name);

        if (userbyname != undefined) {
            return{ message : "username already registered"};
        }

        const response = await createrusermodel( _name , _username , _password , _cpf );

        return response;

    }
    catch(err) {
        return { message: 'Something went wrong' };
    }
}