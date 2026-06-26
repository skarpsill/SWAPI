---
title: "Get Transforms of Assembly Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transforms_of_Assembly_Components_Example_VB.htm"
---

# Get Transforms of Assembly Components Example (VBA)

This example shows how to recursively retrieve the transform for each
child component in an assembly.

'-----------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Assembly is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Assembly is fully resolved.

'

' Postconditions: None

'

' Notes:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Root component does not have a name

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Root component has a NULL transform, that is, no rotation,

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}translation,
or scaling

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(3)
All child component transforms are relative to their

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}root
component

'

'-----------------------------------------------

Option Explicit

Sub OutputCompXform _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swComp
As SldWorks.Component2, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nLevel
As Long _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vChildkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swChildCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sPadStrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCompXformkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vXformkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To nLevel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sPadStr
= sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Null for root component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCompXform = swComp.Transform2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swCompXform Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vXform
= swCompXform.ArrayData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Root component has no name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "Component = " & swComp.Name2 & "
(" & swComp.ReferencedConfiguration& ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Supprkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swComp.IsSuppressed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Hiddenkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= "
& swComp.IsHidden(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rot1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= ("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(0))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(1))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(2))
+ ")" _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rot2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= ("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(3))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(4))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(5))
+ ")" _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rot3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= ("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(6))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(7))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(8))
+ ")" _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Trans
= (" + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(9))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(10))
+ ", " + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vXform(11))
+ ")" _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Scale
= " + Str(vXform(12))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Recurse into subassembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vChild
= swComp.GetChildren

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vChild)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swChildComp = vChild(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputCompXform
swChildComp, nLevel + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swConfkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.configuration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swRootCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swConf = swModel.GetActiveConfiguration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swRootComp = swConf.GetRootComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputCompXform
swRootComp, 0

End Sub

'---------------------------------------
