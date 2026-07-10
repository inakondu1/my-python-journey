
'''
🏋️ Your ChallengeLet's use these to solve a real-world packaging problem. 
Imagine you have a factory that packs eggs into cartons. 
Each carton holds exactly 12 eggs.Write a script that:Asks the user for a total number
 of eggs (e.g., 27) using int(input()).Uses floor division (//) to calculate how many
  full cartons you can completely fill.Uses modulus (%) to calculate how many loose 
  eggs are left over.Prints both results.
  '''
user = int(input("what is the total numbers of eggs: "))
cartons_of_egg = 12

carton_file =  user // cartons_of_egg
left_over = user % cartons_of_egg 
print ('full cartons of eggs', carton_file)
print('left over eggs', left_over)