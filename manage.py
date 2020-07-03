import docker as d


#client=d.from_env(environment={'DOCKER_HOST':'tcp://23.236.60.48:2375'})
client=d.DockerClient(base_url='tcp://23.236.60.48:2375')
containers=client.containers.list(all=True)
#print(containers)

def list_containers():
    containers=client.containers.list(all=True)
    container_list=[]
    for container in containers:
        cont_dict = {}
        cont_dict={'Id':container.short_id,
                   'name':container.name,
                   'status':container.status
                   }
        container_list.append(cont_dict)
    return container_list

def list_images():
    images=client.images.list(all=True)
    images_list=[]
    for image in images:
        image_dict = {}
        image_dict={'Id':image.short_id,
                    'tags':'No Tag' if len(image.tags) == 0 else image.tags
                    }

        images_list.append(image_dict)
    return images_list


def manage_container(action,container_id):
    container=client.containers.get(container_id)
    if action =='Stop':
        container.stop()
    elif action == 'Start' :
        container.start()
    else:
        container.stop()
        container.remove()




print(list_containers())




#print(client.images.list(all=True))

