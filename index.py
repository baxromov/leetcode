n = 5
"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
"""
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print('*', end=" ")
#     print()

"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print('*', end=" ")
#     print()
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
# for i in range(n):
#     for j in range(1, n - i):
#         print(' ', end=" ")
#     for j in range(i + 1):
#         print('*', end=" ")
#     print()

"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end=" ")
#     print()

"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

"""
# for i in range(n, 0, -1):
#     for j in range(1, n - i + 1):
#         print(' ', end=" ")
#     for j in range(i):
#         print('*', end=" ")
#     print()

"""
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
"""
# for i in range(n):
#     for j in range(n - i):
#         print('', end=" ")
#     for j in range(i + 1):
#         print('*', end=" ")
#     print()


"""
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""
# for i in range(n, 0, -1):
#     for j in range(n - i + 1):
#         print('', end=" ")
#     for j in range(i):
#         print('*', end=" ")
#     print()


"""
*         
  *       
    *     
      *   
        *
"""

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i == j:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()

"""
        * 
      * 
    * 
  * 
* 

"""
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         if i == j:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
#
# for i in range(n):
#     for j in range(i + 1):
#         if j == 0 or j == n - 1 or i == n - 1:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()


"""
*  *  *  *  *  
*           *  
*           *  
*           *  
*  *  *  *  * 
"""
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()
