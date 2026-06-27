---
title: "Mate::GetMateDimensionValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetMateDimensionValue.htm"
---

# Mate::GetMateDimensionValue

This method is obsolete and has been superseded
by[Mate2::DisplayDimension2](sldworksAPI.chm::/Mate2/Mate2__DisplayDimension2.htm).

Description

This method gets the mate dimension value. This value is either a distance
in meters or an angle in radians based on the mate type. If this mate
does not support a dimensional value, then 0 is returned.

Syntax (OLE Automation)

retval = Mate.GetMateDimensionValue
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray, which is an array of one double containing
the dimensional value for this mate; this value is either a distance in
meters or an angle in radians based on the mate type |
| --- | --- | --- |

Syntax (COM)

status = Mate->IGetMateDimensionValue
( &dimValue )

(Table)=========================================================

| Output: | (double) dimValue | Pointer to a double containing the dimensional value for this mate;
this value is either a distance in meters or an angle in radians based
on the mate type |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To determine the mate type, see Mate::GetMateParams.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Mate_Object$$**$$ZGetInfoMate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Mate\Mate__GetMateDimensionValue.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
