---
title: "ModelDoc2::GetMassProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetMassProperties2.htm"
---

# ModelDoc2::GetMassProperties2

This method is obsolete and has been superseded
by[ModelDocExtension::GetMassProperties](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetMassProperties.htm).

Description

This method returns the mass properties of
the current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc2.GetMassProperties2 ( &status
)

(Table)=========================================================

| Output: | (long) status | Status of the mass property results as defined
in swMassPropertiesStatus_e |
| --- | --- | --- |
| Return: | (VARIANT) retval | a VARIANT of type SafeArray of doubles |

Syntax (COM)

status = ModelDoc2->IGetMassProperties2 ( &status,
&mPropsData )

(Table)=========================================================

| Output: | (long) status | Status of the mass property results as defined
in swMassPropertiesStatus_e |
| --- | --- | --- |
| Input: | (double) mPropsData | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a zero-based array of doubles
as follows:

[CenterOfMassX, CenterOfMassY, CenterOfMassZ,
Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ]

Yu can obtain the density currently used by the
SolidWorks part by using SldWorks::GetUserPreferencDoubleValue. If the
density has not been explicitly set by the end-user, then a value of 1.0
is used. You can also derive the density of the body using the following
calculation:

Density = ( Mass / Volume )

Consistent with all other API functions, units
returned are metric unless explicitly specified otherwise/

(Table)=========================================================

| If this object is... | Then... |
| --- | --- |
| An assembly | SolidWorks
does not include any suppressed components in the mass property analysis.
See Component2::GetSuppression to determine the state of each assembly
component. This
method returns the moments of inertia (MOI) about the assembly center-of-gravity
coordinate system aligned with the assembly axes. |
| A part | The calculated origin for the returned values are based on the default
coordinate systems of the model document. They are not based on the selected
coordinate system. |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__GetMassProperties2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__GetMassProperties2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
