def invert_resourse_dict(resource_dictionary):
    new_dictionary = {}
    
    for resource_group, resources in resource_dictionary.items():
        for resource in resources:
            if resource in new_dictionary:
                new_dictionary[resource].append(resource_group)
                
            else:
                new_dictionary[resource] = [resource_group]
                
            return(new_dictionary)
        
print(invert_resourse_dict({"hard drives": ["IDE HDDs","SCSI HDDs"], "PC parts":["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))