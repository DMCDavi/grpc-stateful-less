/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     google/api/httpbody.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#include <stddef.h>
#include "upb/msg_internal.h"
#include "google/api/httpbody.upb.h"
#include "google/protobuf/any.upb.h"

#include "upb/port_def.inc"

static const upb_MiniTable_Sub google_api_HttpBody_submsgs[1] = {
  {.submsg = &google_protobuf_Any_msginit},
};

static const upb_MiniTable_Field google_api_HttpBody__fields[3] = {
  {1, UPB_SIZE(0, 0), 0, 0, 9, kUpb_FieldMode_Scalar | (upb_FieldRep_StringView << upb_FieldRep_Shift)},
  {2, UPB_SIZE(8, 16), 0, 0, 12, kUpb_FieldMode_Scalar | (upb_FieldRep_StringView << upb_FieldRep_Shift)},
  {3, UPB_SIZE(16, 32), 0, 0, 11, kUpb_FieldMode_Array | (upb_FieldRep_Pointer << upb_FieldRep_Shift)},
};

const upb_MiniTable google_api_HttpBody_msginit = {
  &google_api_HttpBody_submsgs[0],
  &google_api_HttpBody__fields[0],
  UPB_SIZE(24, 48), 3, upb_ExtMode_NonExtendable, 3, 255, 0,
};

static const upb_MiniTable *messages_layout[1] = {
  &google_api_HttpBody_msginit,
};

const upb_MiniTable_File google_api_httpbody_proto_upb_file_layout = {
  messages_layout,
  NULL,
  NULL,
  1,
  0,
  0,
};

#include "upb/port_undef.inc"

