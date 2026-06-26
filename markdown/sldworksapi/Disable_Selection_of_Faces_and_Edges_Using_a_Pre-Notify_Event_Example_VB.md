---
title: "Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VB.htm"
---

# Disable Selection of Faces and Edges Using a Pre-Notify Event Example (VBA)

This example shows how to disable the interactive selection of these entities
using a pre-notify event:

- faces in part and assembly documents
- edges in drawing documents

```
'------------------------------------
' Preconditions:
' 1. Copy Module into the macro.
' 2. Click Insert > Class Module and copy Class1 into
'    that module.
' 3. Click Insert > Class Module and copy Class2 into
'    that module.
' 4. Click Insert > Class Module and copy Class3 into
'    that module.
' 5. Open a part, assembly, or drawing.
'
'
' Postconditions:
' 1. Disables interactively selecting faces in
'    a part or assembly.
'    - or -
'    Disables interactively selecting edges in a
'    drawing.
' 2. Click the Reset button in the Microsoft Visual
'    Basic IDE to re-enable the interactive selection
'    of faces in a part or assembly or edges
'    in a drawing.
'----------------------------------------
'Module
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim partDoc As New Class1
Dim assemblyDoc As New Class2
Dim drawingDoc As New Class3
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Determine the document type, then
    ' execute its corresponding class module
    If swModel.GetType = swDocPART Then
        partDoc.init swModel
    ElseIf swModel.GetType = swDocASSEMBLY Then
        assemblyDoc.init swModel
    ElseIf swModel.GetType = swDocDRAWING Then
        drawingDoc.init swModel
    End If
```

```
End Sub
```

```vb
Back to top
```

###### ' Class1 Public WithEvents doc As partDoc

```vb
Public Function init(ByRef docIn As Object)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set doc = docIn
 End Function

Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Disable the selection of faces in this part
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SelectionType = swSelFACES Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doc_UserSelectionPreNotify = True
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Function
```

Back to top

###### 'Class2

```vb
Public WithEvents doc As assemblyDoc

Public Function init(ByRef docIn As Object)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set doc = docIn
End Function

Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Disable selection of faces in this assembly
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SelectionType = swSelFACES Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doc_UserSelectionPreNotify = True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Function
```

Back to top

###### 'Class3

```vb
Public WithEvents doc As drawingDoc

Public Function init(ByRef docIn As Object)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set doc = docIn
End Function

Private Function doc_UserSelectionPreNotify(ByVal SelectionType As Long) As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Disable the selection of edges in drawings
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SelectionType = swSelEDGES Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doc_UserSelectionPreNotify = True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Function
Back to top
```
