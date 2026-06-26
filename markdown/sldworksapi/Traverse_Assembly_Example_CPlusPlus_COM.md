---
title: "Traverse Assembly Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_Example_CPlusPlus_COM.htm"
---

# Traverse Assembly Example (C++ COM)

This example shows how to traverse an assembly
using the IComponent2 object. The method IComponent2::IGetChildren returns
an array, so this code must be used in an in-process DLL. Otherwise, use
the method IComponent2::GetChildren that returns a VARIANT.

void GetModelAssembly(ISldWorks* m_pSldWorks)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCONFIGURATION
pConfiguration = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCOMPONENT
pRootComponent = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
pModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres = S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
RecurseLevel = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= m_pSldWorks->get_IActiveDoc2(
&pModelDoc );kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve model document pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
S_OK != hres || pModelDoc == NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the active configuration and root component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
( pModelDoc->IGetActiveConfiguration(&pConfiguration)
== S_OK )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
( pConfiguration->IGetRootComponent(&pRootComponent)
== S_OK )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
MyString;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TraverseChildren(RecurseLevel,&MyString,pRootComponent);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pRootComponent->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Display the structure in a message box

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AfxMessageBox
(MyString);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pConfiguration->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//////////////////////////////////////////////////////////////////////////

// Function: TraverseChildren

// Arguments: RecurseLevel - Level of recursion

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyString
- Textural record of assembly

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pComponent
- Component to traverse

// Return: Number of children

// Description: Perform any operations specific to the
component, then

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
the component has children, recursively call

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}this
function for each child.

//////////////////////////////////////////////////////////////////////////

int TraverseChildren(long RecurseLevel, CString* MyString,
LPCOMPONENT pComponent)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCOMPONENT*
pChildren = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nChildren;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Name;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres =
S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOCkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve the component name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(RecurseLevel==0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Special case of top-level components

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= m_pSldWorks->get_IActiveDoc(
&pModelDoc );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
S_OK == hres || pModelDoc != NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->GetTitle(&Name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the component name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pComponent->get_Name(&Name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
S_OK == hres && Name != NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
tempstr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for(
i=1; I<=RecurseLevel; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tempstr
+= " ";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
Tmp(Name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tempstr
+= Tmp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tempstr
+= "\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*MyString
= *MyString + tempstr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RecurseLevel++;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pComponent->IGetChildrenCount(&nChildren);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Check if this component has children

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
( S_OK == hres || nChildren > 0 )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pChildren
= new LPCOMPONENT [nChildren];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pComponent->IGetChildren((LPCOMPONENT**)&pChildren);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
== hres)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Recursively traverse the children

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
( i=0; i<nChildren; i++ )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TraverseChildren(RecurseLevel,MyString,pChildren[i]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pChildren[i]->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] pChildren;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RecurseLevel--;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
nChildren;

}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
