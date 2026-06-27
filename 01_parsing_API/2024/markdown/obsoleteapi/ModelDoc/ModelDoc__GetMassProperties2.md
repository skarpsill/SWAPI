---
title: "ModelDoc::GetMassProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetMassProperties2.htm"
---

# ModelDoc::GetMassProperties2

This
method is obsolete and has been superseded by[ModelDoc2::GetMassProperties2](../ModelDoc2/ModelDoc2__GetMassProperties2.htm).

Description

This method returns the mass properties of
the current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc.GetMassProperties2 ( &status
)

(Table)=========================================================

| Output: | (long) status | Status of the mass property results as defined
in swMassPropertiesStatus_e |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray |

Syntax (COM)

status = ModelDoc->GetMassProperties2 ( &status,
&mPropsData )

(Table)=========================================================

| Output: | (long) status | Status of the mass property results as defined
in swMassPropertiesStatus_e |
| --- | --- | --- |
| Input: | (double) mPropsData | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a 0-based array of doubles
as follows:

[kadov_tag{{<spaces>}}CenterOfMassX,
CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ,
MomXY, MomZX, MomYZkadov_tag{{<spaces>}}]

To obtain the density currently being used by the
SolidWorks part, callkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SldWorks::GetUserPreferencDoubleValue.
If the user has not explicitly set the density, then a value of 1.0 will
be used. You can also derive the density of the body using the following
calculation:

Density = ( Mass / Volume )

Consistent with all other API functions, units
returned will be metric unless explicitly specified.

If this ModelDoc object is an assembly, then any
suppressed components are not included in the mass property analysis.
Use Component::GetSuppression to determine the state for each of the assembly's
components.

NOTE:The
calculated origin for the returned values is based on the default coordinate
systems of the ModelDoc. It is not based on the a selected coordinate
system.

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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetMassProperties2.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetMassProperties2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
