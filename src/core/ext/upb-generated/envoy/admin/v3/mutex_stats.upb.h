/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     envoy/admin/v3/mutex_stats.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#ifndef ENVOY_ADMIN_V3_MUTEX_STATS_PROTO_UPB_H_
#define ENVOY_ADMIN_V3_MUTEX_STATS_PROTO_UPB_H_

#include "upb/msg_internal.h"
#include "upb/decode.h"
#include "upb/decode_fast.h"
#include "upb/encode.h"

#include "upb/port_def.inc"

#ifdef __cplusplus
extern "C" {
#endif

struct envoy_admin_v3_MutexStats;
typedef struct envoy_admin_v3_MutexStats envoy_admin_v3_MutexStats;
extern const upb_MiniTable envoy_admin_v3_MutexStats_msginit;



/* envoy.admin.v3.MutexStats */

UPB_INLINE envoy_admin_v3_MutexStats* envoy_admin_v3_MutexStats_new(upb_Arena* arena) {
  return (envoy_admin_v3_MutexStats*)_upb_Message_New(&envoy_admin_v3_MutexStats_msginit, arena);
}
UPB_INLINE envoy_admin_v3_MutexStats* envoy_admin_v3_MutexStats_parse(const char* buf, size_t size, upb_Arena* arena) {
  envoy_admin_v3_MutexStats* ret = envoy_admin_v3_MutexStats_new(arena);
  if (!ret) return NULL;
  if (upb_Decode(buf, size, ret, &envoy_admin_v3_MutexStats_msginit, NULL, 0, arena) != kUpb_DecodeStatus_Ok) {
    return NULL;
  }
  return ret;
}
UPB_INLINE envoy_admin_v3_MutexStats* envoy_admin_v3_MutexStats_parse_ex(const char* buf, size_t size,
                           const upb_ExtensionRegistry* extreg,
                           int options, upb_Arena* arena) {
  envoy_admin_v3_MutexStats* ret = envoy_admin_v3_MutexStats_new(arena);
  if (!ret) return NULL;
  if (upb_Decode(buf, size, ret, &envoy_admin_v3_MutexStats_msginit, extreg, options, arena) !=
      kUpb_DecodeStatus_Ok) {
    return NULL;
  }
  return ret;
}
UPB_INLINE char* envoy_admin_v3_MutexStats_serialize(const envoy_admin_v3_MutexStats* msg, upb_Arena* arena, size_t* len) {
  return upb_Encode(msg, &envoy_admin_v3_MutexStats_msginit, 0, arena, len);
}
UPB_INLINE char* envoy_admin_v3_MutexStats_serialize_ex(const envoy_admin_v3_MutexStats* msg, int options,
                                 upb_Arena* arena, size_t* len) {
  return upb_Encode(msg, &envoy_admin_v3_MutexStats_msginit, options, arena, len);
}
UPB_INLINE uint64_t envoy_admin_v3_MutexStats_num_contentions(const envoy_admin_v3_MutexStats* msg) {
  return *UPB_PTR_AT(msg, UPB_SIZE(0, 0), uint64_t);
}
UPB_INLINE uint64_t envoy_admin_v3_MutexStats_current_wait_cycles(const envoy_admin_v3_MutexStats* msg) {
  return *UPB_PTR_AT(msg, UPB_SIZE(8, 8), uint64_t);
}
UPB_INLINE uint64_t envoy_admin_v3_MutexStats_lifetime_wait_cycles(const envoy_admin_v3_MutexStats* msg) {
  return *UPB_PTR_AT(msg, UPB_SIZE(16, 16), uint64_t);
}

UPB_INLINE void envoy_admin_v3_MutexStats_set_num_contentions(envoy_admin_v3_MutexStats *msg, uint64_t value) {
  *UPB_PTR_AT(msg, UPB_SIZE(0, 0), uint64_t) = value;
}
UPB_INLINE void envoy_admin_v3_MutexStats_set_current_wait_cycles(envoy_admin_v3_MutexStats *msg, uint64_t value) {
  *UPB_PTR_AT(msg, UPB_SIZE(8, 8), uint64_t) = value;
}
UPB_INLINE void envoy_admin_v3_MutexStats_set_lifetime_wait_cycles(envoy_admin_v3_MutexStats *msg, uint64_t value) {
  *UPB_PTR_AT(msg, UPB_SIZE(16, 16), uint64_t) = value;
}

extern const upb_MiniTable_File envoy_admin_v3_mutex_stats_proto_upb_file_layout;

#ifdef __cplusplus
}  /* extern "C" */
#endif

#include "upb/port_undef.inc"

#endif  /* ENVOY_ADMIN_V3_MUTEX_STATS_PROTO_UPB_H_ */
