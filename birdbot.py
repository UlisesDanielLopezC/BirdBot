import discord #importando los comandos de discord

client = discord.Client() #creando un objeto tipo cliente

#un evento basado en un "callback"
@client.event
#imprimir el texto cuando el bot entre en funcionamiento
async def on_ready():
    print('En funcionamiento: {0.user}'.format(client))

@client.event
#se declara el evento que tiene por parametro un mensaje
async def on_message(mensaje):
    #si el usuario que escribió el mensaje es el propio bot:
    #no se ejecuta nada en especial
    if mensaje.author == client.user:
        return

    #si el mensaje enviado empieza con "+ACT"
    if mensaje.content.startswith('+ACT'):

        #await mensaje.channel.send('BirdBot te saluda')

        #Se borra la linea "+ACT" del mensaje
        respuesta = mensaje.content
        accion = respuesta.split()
        del accion[0]

        act = ""
        for palabra in accion:
            act += " "
            act += palabra

        #Se envia un mensaje al mismo canal donde fue llamado el bot con la accion escrita
        await mensaje.channel.send('BirdBot ha empezado a' + act + ".")

my_secret = os.environ['TheToken']
client.run(my_secret)