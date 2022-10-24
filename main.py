from SymbolTable import SymbolTable

if __name__ == '__main__':
    st = SymbolTable()
    print(st.add("ioana"))
    print(st.add("marius"))
    print(st.add("vali"))
    print(st.add("cosmin"))
    print(st.add("2"))
    st.add(5)
    print(st)

    print(st.get("ioana"))
    print(st.get("2"))
    print(st.get(5))
