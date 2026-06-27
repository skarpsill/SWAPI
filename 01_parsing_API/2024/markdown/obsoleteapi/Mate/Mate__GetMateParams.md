---
title: "Mate::GetMateParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetMateParams.htm"
---

# Mate::GetMateParams

This method is obsolete and has not been superseded.

Description

This method gets the assembly mate parameters.

Syntax (OLE Automation)

retval = Mate.GetMateParams ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing three longs:mateType, alignFlag,
and canBeFlipped (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Mate->IGetMateParams (
&mateType, &alignFlag, &canBeFlipped )

(Table)=========================================================

| Output: | (long) mateType | The type of the mate |
| --- | --- | --- |
| Output: | (long) alignFlag | TRUE or FALSE (see Remarks ) |
| Output: | (long) canBeFlipped | TRUE or FALSE (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

- alignFlag-1 if the mated entities are aligned, 2 if the mated entities are
  anti-aligned.
- canBeFlipped-2 if the mated entities can be flipped, 1 otherwise. This is
  only useful for mating conditions with dimensional values.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Mate_Object$$**$$ZGetInfoMate$$**$$ZMateRelationShips$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Mate\Mate__GetMateParams.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
