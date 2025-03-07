# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import packaging.version

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.translate_v3.types import translation_service
from google.longrunning import operations_pb2  # type: ignore
from .base import TranslationServiceTransport, DEFAULT_CLIENT_INFO
from .grpc import TranslationServiceGrpcTransport


class TranslationServiceGrpcAsyncIOTransport(TranslationServiceTransport):
    """gRPC AsyncIO backend transport for TranslationService.

    Provides natural language translation operations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "translate.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "translate.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def translate_text(
        self,
    ) -> Callable[
        [translation_service.TranslateTextRequest],
        Awaitable[translation_service.TranslateTextResponse],
    ]:
        r"""Return a callable for the translate text method over gRPC.

        Translates input text and returns translated text.

        Returns:
            Callable[[~.TranslateTextRequest],
                    Awaitable[~.TranslateTextResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "translate_text" not in self._stubs:
            self._stubs["translate_text"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/TranslateText",
                request_serializer=translation_service.TranslateTextRequest.serialize,
                response_deserializer=translation_service.TranslateTextResponse.deserialize,
            )
        return self._stubs["translate_text"]

    @property
    def detect_language(
        self,
    ) -> Callable[
        [translation_service.DetectLanguageRequest],
        Awaitable[translation_service.DetectLanguageResponse],
    ]:
        r"""Return a callable for the detect language method over gRPC.

        Detects the language of text within a request.

        Returns:
            Callable[[~.DetectLanguageRequest],
                    Awaitable[~.DetectLanguageResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "detect_language" not in self._stubs:
            self._stubs["detect_language"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/DetectLanguage",
                request_serializer=translation_service.DetectLanguageRequest.serialize,
                response_deserializer=translation_service.DetectLanguageResponse.deserialize,
            )
        return self._stubs["detect_language"]

    @property
    def get_supported_languages(
        self,
    ) -> Callable[
        [translation_service.GetSupportedLanguagesRequest],
        Awaitable[translation_service.SupportedLanguages],
    ]:
        r"""Return a callable for the get supported languages method over gRPC.

        Returns a list of supported languages for
        translation.

        Returns:
            Callable[[~.GetSupportedLanguagesRequest],
                    Awaitable[~.SupportedLanguages]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_supported_languages" not in self._stubs:
            self._stubs["get_supported_languages"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/GetSupportedLanguages",
                request_serializer=translation_service.GetSupportedLanguagesRequest.serialize,
                response_deserializer=translation_service.SupportedLanguages.deserialize,
            )
        return self._stubs["get_supported_languages"]

    @property
    def translate_document(
        self,
    ) -> Callable[
        [translation_service.TranslateDocumentRequest],
        Awaitable[translation_service.TranslateDocumentResponse],
    ]:
        r"""Return a callable for the translate document method over gRPC.

        Translates documents in synchronous mode.

        Returns:
            Callable[[~.TranslateDocumentRequest],
                    Awaitable[~.TranslateDocumentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "translate_document" not in self._stubs:
            self._stubs["translate_document"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/TranslateDocument",
                request_serializer=translation_service.TranslateDocumentRequest.serialize,
                response_deserializer=translation_service.TranslateDocumentResponse.deserialize,
            )
        return self._stubs["translate_document"]

    @property
    def batch_translate_text(
        self,
    ) -> Callable[
        [translation_service.BatchTranslateTextRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the batch translate text method over gRPC.

        Translates a large volume of text in asynchronous
        batch mode. This function provides real-time output as
        the inputs are being processed. If caller cancels a
        request, the partial results (for an input file, it's
        all or nothing) may still be available on the specified
        output location.
        This call returns immediately and you can
        use google.longrunning.Operation.name to poll the status
        of the call.

        Returns:
            Callable[[~.BatchTranslateTextRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_translate_text" not in self._stubs:
            self._stubs["batch_translate_text"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/BatchTranslateText",
                request_serializer=translation_service.BatchTranslateTextRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_translate_text"]

    @property
    def batch_translate_document(
        self,
    ) -> Callable[
        [translation_service.BatchTranslateDocumentRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the batch translate document method over gRPC.

        Translates a large volume of document in asynchronous
        batch mode. This function provides real-time output as
        the inputs are being processed. If caller cancels a
        request, the partial results (for an input file, it's
        all or nothing) may still be available on the specified
        output location.
        This call returns immediately and you can use
        google.longrunning.Operation.name to poll the status of
        the call.

        Returns:
            Callable[[~.BatchTranslateDocumentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_translate_document" not in self._stubs:
            self._stubs["batch_translate_document"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/BatchTranslateDocument",
                request_serializer=translation_service.BatchTranslateDocumentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_translate_document"]

    @property
    def create_glossary(
        self,
    ) -> Callable[
        [translation_service.CreateGlossaryRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create glossary method over gRPC.

        Creates a glossary and returns the long-running operation.
        Returns NOT_FOUND, if the project doesn't exist.

        Returns:
            Callable[[~.CreateGlossaryRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_glossary" not in self._stubs:
            self._stubs["create_glossary"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/CreateGlossary",
                request_serializer=translation_service.CreateGlossaryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_glossary"]

    @property
    def list_glossaries(
        self,
    ) -> Callable[
        [translation_service.ListGlossariesRequest],
        Awaitable[translation_service.ListGlossariesResponse],
    ]:
        r"""Return a callable for the list glossaries method over gRPC.

        Lists glossaries in a project. Returns NOT_FOUND, if the project
        doesn't exist.

        Returns:
            Callable[[~.ListGlossariesRequest],
                    Awaitable[~.ListGlossariesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_glossaries" not in self._stubs:
            self._stubs["list_glossaries"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/ListGlossaries",
                request_serializer=translation_service.ListGlossariesRequest.serialize,
                response_deserializer=translation_service.ListGlossariesResponse.deserialize,
            )
        return self._stubs["list_glossaries"]

    @property
    def get_glossary(
        self,
    ) -> Callable[
        [translation_service.GetGlossaryRequest],
        Awaitable[translation_service.Glossary],
    ]:
        r"""Return a callable for the get glossary method over gRPC.

        Gets a glossary. Returns NOT_FOUND, if the glossary doesn't
        exist.

        Returns:
            Callable[[~.GetGlossaryRequest],
                    Awaitable[~.Glossary]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_glossary" not in self._stubs:
            self._stubs["get_glossary"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/GetGlossary",
                request_serializer=translation_service.GetGlossaryRequest.serialize,
                response_deserializer=translation_service.Glossary.deserialize,
            )
        return self._stubs["get_glossary"]

    @property
    def delete_glossary(
        self,
    ) -> Callable[
        [translation_service.DeleteGlossaryRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete glossary method over gRPC.

        Deletes a glossary, or cancels glossary construction if the
        glossary isn't created yet. Returns NOT_FOUND, if the glossary
        doesn't exist.

        Returns:
            Callable[[~.DeleteGlossaryRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_glossary" not in self._stubs:
            self._stubs["delete_glossary"] = self.grpc_channel.unary_unary(
                "/google.cloud.translation.v3.TranslationService/DeleteGlossary",
                request_serializer=translation_service.DeleteGlossaryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_glossary"]


__all__ = ("TranslationServiceGrpcAsyncIOTransport",)
