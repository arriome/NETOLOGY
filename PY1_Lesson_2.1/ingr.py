with open('ingr_data.txt') as f:
    def dish_build():
      dish1=f.readline()
      print('Блюдо:',dish1)
      count = int(f.readline())
      print('Количество ингридиентов:',count)
      i=0
      while i < count:
         ingridients = f.readline() 
         ingridients_list = ingridients.split('|')
         print(ingridients_list)
         i = i+1
      d_local1 = dict.fromkeys(['ingridient_name','quantity','measure'],ingridients_list) #пытаемся построить список из словарей под ключ - название блюда  
      d_local2 = {dish1:ingridients_list}
      return dish1,ingridients_list, d_local2    #проходим первое блюдо отдельно, т.к. оно не отделено пустой строкой - разделителем
    dish_first,ingr_first,d=dish_build()        #проходим остальные блюда
    d2=dict.fromkeys(dish_first,d)
    print('СПИСОК ПЕРВОГО БЛЮДА:',d2)
    
    for line in f:     
       if (len(line)-1) == 0:
          dish,ingr,d=dish_build()
          print('СПИСКИ БЛЮД: ',d)
          

         
  #  cook_book = {
  # 'яйчница': [
   #  {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
   #  {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
   #  ],  
     
        


        

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
          new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()

