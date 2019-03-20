# array<struct<name:string,address:map<int,int>,credits:array<int>>>
# [ {"name":"ravi",{23,06,43,11,28,78},[23,45,56,6,67]} ,6,43,11,28,78},[23,45,56,6,67]} ,{"name":"ravi",{23,06,43,11,28,78},[23,45,56,6,67]}]
# array(   named_struct("name","ravi",map(23,06,43,11,28,78),array(23,45,56,6,67)), , )
# select 'c1_val',named_struct('c2_a',array(cast (null as string)),'c2_c',cast (null as string)),array(named_struct('c3_a',cast (null as string) ,'c3_b',cast (null as string))) from z_dummy;
#
i=0
stmt=""
l=[]
def create_structure(struct):
    j=0
    while j<len(struct):
        if struct[j:j+6]=="array<":
            c=1
            for _ in struct[j+6:]:
                if _==''







structure = "array<struct<name:string,address:map<int,int>,credits:array<int>>>"
data = '[{"name":"ravi",{23,06,43,11,28,78},[23,45,56,6,67]},{"name":"ravi",{23,06,43,11,28,78},[23,45,56,6,67]},{"name":"ravi",{23,06,43,11,28,78},[23,45,56,6,67]}]'
print(create_insert(structure, data))

