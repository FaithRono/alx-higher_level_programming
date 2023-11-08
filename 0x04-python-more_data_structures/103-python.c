#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");

    if (PyBytes_Check(p)) {
        size = PyBytes_GET_SIZE(p);
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", bytes->ob_sval);
        printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
        for (i = 0; i < size + 1 && i < 10; i++) {
            printf("%02x%c", bytes->ob_sval[i],
                   i + 1 < size + 1 && i + 1 < 10 ? ' ' : '\n');
        }
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;

    printf("[*] Python list info\n");

    if (PyList_Check(p)) {
        size = Py_SIZE(p);
        allocated = list->allocated;
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocated);
        for (i = 0; i < size; i++) {
            PyObject *element = list->ob_item[i];
            printf("Element %ld: %s\n", i,
                   PyBytes_Check(element) ? "bytes" :
                   PyList_Check(element) ? "list" :
                   PyFloat_Check(element) ? "float" :
                   PyLong_Check(element) ? "int" :
                   PyTuple_Check(element) ? "tuple" :
                   PyUnicode_Check(element) ? "str" : "?");
            if (PyBytes_Check(element)) {
                print_python_bytes(element);
            }
        }
    }
}

