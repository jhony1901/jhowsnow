import {createrusermodel , findusermodelbycpf, findusermodelbyusername}  from "../model/user";

export async function createUser(_username:string , _password:string , _confirmPassword:string , _cpf:string , _name = "") {
    // Realizar verificações em atributos Únicos das tabelas.
    // Verificar se os valores já estão cadastrados no banco de dados
    try {
        if( _password != _confirmPassword ) {
            return { status:400, message: 'Passwords dont match' };
        }

        //Verificar username e cpf
        const userbycpf = await findusermodelbycpf(_cpf);

        if (userbycpf != undefined ) {
            return{ status:403, message : "cpf already registered"};
        }
        const userbyname = await findusermodelbyusername(_name);

        if (userbyname != undefined) {
            return{ status:403, message : "username already registered"};
        }

        const response = await createrusermodel( _name , _username , _password , _cpf );

        return {status:201, message:'User registered', data:response  };

    }
    catch(err) {
        return { status:500, message: 'Something went wrong' };
    }
}