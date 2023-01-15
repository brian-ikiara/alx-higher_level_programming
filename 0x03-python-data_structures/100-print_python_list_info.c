#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Function
 * @p: Python object
 *
 * Description: Prints information about a Python object; in
 * our case, the list object. I know Betty is complaining of no
 * such header file as "Python.h", but it'll be compiled with
 * the following: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 * -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 * 100-print_python_list_info.c
 * Return: void.
 * On error, stderr.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p), i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %li: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
