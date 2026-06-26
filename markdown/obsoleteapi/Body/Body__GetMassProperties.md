---
title: "Body::GetMassProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetMassProperties.htm"
---

# Body::GetMassProperties

This
method is obsolete and has been superseded by[Body2::GetMassProperties](sldworksAPI.chm::/Body2/Body2__GetMassProperties.htm).

Description

This method returns the mass properties of this Body object. This is
intended for obtaining the mass properties of temporary body objects but
may also be used with the SolidWorks Body object that is created by the
user.

To get the mass properties of the SolidWorks Body object that is created
by the user, you can also use[ModelDoc::GetMassProperties](../ModelDoc/ModelDoc__GetMassProperties.htm),
which uses the density currently set for the body's material.

Syntax (OLE Automation)

retval
= Body.GetMassProperties ( density)

(Table)=========================================================

| Input: | (double)
density | Density
to be used for the mass property calculations on this body |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray |

Syntax (COM)

status
= Body->IGetMassProperties ( density, retval )

(Table)=========================================================

| Input: | (double)
density | Density
to be used for the mass property calculations on this body |
| --- | --- | --- |
| Output: | (double*)
retval | Pointer
to an array of doubles |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The
return value is an array of doubles as follows:

[CenterOfMassX,
CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ,
MomXY, MomZX, MomYZ]

You can use SldWorks::GetUserPreferenceDoubleValue
to get the density for a SolidWorks part.

This method returns
metric units unless explicitly specified.

SolidWorks returns
information (such as the center of mass) in relation to where the body
was created. For example, if you create a block in a part file that is
centered at (0,0,0), then the center of mass is returned as (0,0,0). If
this part is then used at some random location within an assembly and
you use Component2::GetBody to get the body from the assembly component
object, the center of mass is still returned as (0,0,0). If you need to
determine the body's center of mass in relation to the assembly coordinate
system, you must multiply the component transform with the center of mass
coordinates (see Component::GetXform).

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$Face::GetArea$$**$$GetMassProperties$$**$$SldWorks::GetUserPreferenceDoubleValue$$**$$ZGetInfoBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body\Body__GetMassProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
