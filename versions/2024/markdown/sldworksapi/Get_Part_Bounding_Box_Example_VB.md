---
title: "Get Part Bounding Box Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part_Bounding_Box_Example_VB.htm"
---

# Get Part Bounding Box Example (VBA)

This example shows how to get an accurate bounding box for a open part.

'-----------------------------------------------

'

' Problem:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IPartDoc::GetPartBox
returns an approximate

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bounding
box and cannot be relied upon to be used

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}in
calculations. Typically, the bounding box

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}returned
is larger and not a minimal bounding box.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
best use for IPartDoc::GetPartbox is as a first

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}approximation
to determine whether two parts are intersecting.

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
there is a need for a more accurate bounding

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}box,
then use one based on the display tessellation, which

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gives
a more minimal bounding box.

'

' Preconditions: Part is open.

'

' Postconditions: None

'

'-----------------------------------------------

Option Explicit

Function GetMax _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val1
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val2
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val3
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val4
As Double _

) As Double

' Finds maximum of four values

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMax
= Val1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Val2 > GetMax Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMax
= Val2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Val3 > GetMax Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMax
= Val3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Val4 > GetMax Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMax
= Val4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Function

Function GetMin _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val1
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val2
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val3
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Val4
As Double _

) As Double

' Finds minimum of four values

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMin
= Val1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Val2 < GetMin Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMin
= Val2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Val3 < GetMin Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMin
= Val3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Val4 < GetMin Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetMin
= Val4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Function

Sub ProcessTessTriangles _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vTessTriangles
As Variant, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_max
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_min
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_max
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_min
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_max
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_min
As Double _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vTessTriangles) / (1 * 9) - 1

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Debugging output only

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Pt(" + Str(i) + ") = "

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" (" + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 0)) + "," + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 1)) + "," + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 2)) + ")"

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" (" + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 3)) + "," + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 4)) + "," + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 5)) + ")"

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" (" + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 6)) + "," + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 7)) + "," + _

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vTessTriangles(9
* i + 8)) + ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_max
= GetMax((vTessTriangles(9 * i + 0)), (vTessTriangles(9 * i + 3)), (vTessTriangles(9
* i + 6)), X_max)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_min
= GetMin((vTessTriangles(9 * i + 0)), (vTessTriangles(9 * i + 3)), (vTessTriangles(9
* i + 6)), X_min)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_max
= GetMax((vTessTriangles(9 * i + 1)), (vTessTriangles(9 * i + 4)), (vTessTriangles(9
* i + 7)), Y_max)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_min
= GetMin((vTessTriangles(9 * i + 1)), (vTessTriangles(9 * i + 4)), (vTessTriangles(9
* i + 7)), Y_min)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_max
= GetMax((vTessTriangles(9 * i + 2)), (vTessTriangles(9 * i + 5)), (vTessTriangles(9
* i + 8)), Z_max)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_min
= GetMin((vTessTriangles(9 * i + 2)), (vTessTriangles(9 * i + 5)), (vTessTriangles(9
* i + 8)), Z_min)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

Sub ProcessBodies _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
As Variant, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_max
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_min
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_max
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_min
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_max
As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_min
As Double _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vTessTriangleskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Probably empty if no reference surfaces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vBodies) Then Exit Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vBodies)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBody = vBodies(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swBody.GetFirstFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
Not swFace Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vTessTriangles
= swFace.GetTessTriangles(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ProcessTessTriangles
vTessTriangles, X_max, X_min, Y_max, Y_min, Z_max, Z_min

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swFace.GetNextFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Wend

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
MaxDoublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = 1.79769313486231E+308

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
MinDoublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = -1.79769313486231E+308

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBodieskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBoundBoxkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
X_maxkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
X_minkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Y_maxkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Y_minkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Z_maxkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Z_minkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPart = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Initialise to large/small values

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_max
= MinDouble

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}X_min
= MaxDouble

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_max
= MinDouble

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Y_min
= MaxDouble

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_max
= MinDouble

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Z_min
= MaxDouble

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Solid body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
= swPart.GetBodies2(swSolidBody,
False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ProcessBodies
vBodies, X_max, X_min, Y_max, Y_min, Z_max, Z_min

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Reference surfaces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
= swPart.GetBodies2(swSheetBody,
False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ProcessBodies
vBodies, X_max, X_min, Y_max, Y_min, Z_max, Z_min

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Approximate bounding box

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBoundBox
= swPart.GetPartBox(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Tessellation Quality = " + Str(swModel.GetTessellationQuality)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"PartBox = "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vBoundBox(0)
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vBoundBox(1)
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vBoundBox(2)
* 1000#) + ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vBoundBox(3)
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vBoundBox(4)
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(vBoundBox(5)
* 1000#) + ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"TessBox = "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(X_min
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(Y_min
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(Z_min
* 1000#) + ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}("
+ _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(X_max
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(Y_max
* 1000#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(Z_max
* 1000#) + ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

End Sub

'------------------------------------------
