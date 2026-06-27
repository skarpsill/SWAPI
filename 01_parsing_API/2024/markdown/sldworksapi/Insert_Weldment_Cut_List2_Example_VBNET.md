---
title: "Insert Weldment Cut List Example #2 (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List2_Example_VBNET.htm"
---

# Insert Weldment Cut List Example #2 (VB.NET)

This example shows how to insert a weldment cut list into the FeatureManager
design tree.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\assemblymates\bracket.sldprt.
' 2. Click Tools > Options > System Options > FeatureManager >
'    Solid Bodies > Show > OK.
' 3. Expand the Solid Bodies(1) folder in the FeatureManager design tree
'    and note its contents.
'
' Postconditions:
' 1. Inserts a cut-list-item folder feature containing the specified
'    weldment body.
' 2. Expand the Cut-List-Item1 folder in the Solid Bodies(1) folder
'    in the the FeatureManager design tree to verify step 1.
'
' NOTE: Because this part is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------
```

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Part As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
obj(0) As Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
v As Array

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v
= Part.**GetBodies2**(0, True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(v)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}obj(i)
= CType(v(i), Body2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cutListFeature As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cutListFeature
= Part.**FeatureManager**.InsertWeldmentCutList2(obj)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
