---
title: "ModelDoc2::GetMassProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetMassProperties.htm"
---

# ModelDoc2::GetMassProperties

This
method is obsolete and has be superseded by ModelDoc2::GetMassProperties2 ,

Description

This method returns the mass properties of the
current part or assembly.

Syntax (OLE Automation)

retval = ModelDoc2.GetMassProperties
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetMassProperties
( mPropsData, &retval )

(Table)=========================================================

| Input: | (double) mPropsData | Pointer to an array of doubles |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a 0-based array of doubles as follows:

[CenterOfMassX, CenterOfMassY,
CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX,
MomYZ]

You can obtain the density currently used by the SolidWorks part by
using SldWorks::GetUserPreferencDoubleValue. If the density has not been
explicitly set by the end-user, then a value of 1.0 is used. You can also
derive the density of the body using the following calculation:

Density = (Mass/Volume)

Consistent with all other API functions, units returned are metric unless
explicitly specified otherwise.

If this ModelDoc2 object is an assembly, then any suppressed components
are not included in the mass property analysis. See Component2::GetSuppression
to determine the state for each of the assembly's components.

NOTE: The Calculated origin
for the returned values are based on the default coordinate systems of
the ModelDoc2. They are not based on the a selected coordinate system

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__IGetMassProperties.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__IGetMassProperties.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
