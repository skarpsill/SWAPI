---
title: "Increase Width of Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Increase_Width_of_Text_Example_VB.htm"
---

# Increase Width of Text Example (VBA)

This example shows how to increase the width of the text in a note by
a factor of 2.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Select the note Fixed Face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Increases the width of the text in the selected note
'    by a factor of 2.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'-------------------------------------------------------
```

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.modelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAnnObjkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAnnotationkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Annotation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swTextFormatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.textFormatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dWidthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAnnObj = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAnnotation = swAnnObj.GetAnnotation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTextFormat = swAnnotation.GetTextFormat(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dWidth
= swTextFormat.WidthFactor

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Old width = " & dWidth

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTextFormat.WidthFactor= 2# * dWidth

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swAnnotation.SetTextFormat(0,
False, swTextFormat)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dWidth
= swTextFormat.WidthFactor

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"New width = " & dWidth

End Sub
